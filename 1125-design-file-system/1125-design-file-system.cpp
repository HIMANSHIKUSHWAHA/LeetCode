class FileSystem {
    struct Trie {
        int val;
        unordered_map<string, shared_ptr<Trie>> map;
    };
    shared_ptr<Trie> root;
public:
    FileSystem() {
        root = make_shared<Trie>();
    }
    
    bool createPath(string path, int value) {
        istringstream iss{path};
        string folder;
        string prevFolder;
        shared_ptr<Trie> cur = root;
        shared_ptr<Trie> prev;
        bool newPath = false;
        getline(iss, folder, '/');
        while (getline(iss, folder, '/')) {
            if (cur->map.find(folder) == cur->map.end()) {
                cur->map[folder] = make_shared<Trie>(-1);
                if (newPath) {
                    prev->map.erase(prevFolder);
                    return false;
                }
                newPath = true;
            }
            prevFolder = folder;
            prev = cur;
            cur = cur->map[folder];
        }
        if (!newPath) return false;
        cur->val = value;
        return true;
    }
    
    int get(string path) {
        istringstream iss{path};
        string folder;
        shared_ptr<Trie> cur = root;
        getline(iss, folder, '/');
        while (getline(iss, folder, '/')) {
            if (cur->map.find(folder) == cur->map.end()) {
                return -1;
            }
            cur = cur->map[folder];
        }
        return cur->val;
    }
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem* obj = new FileSystem();
 * bool param_1 = obj->createPath(path,value);
 * int param_2 = obj->get(path);
 */