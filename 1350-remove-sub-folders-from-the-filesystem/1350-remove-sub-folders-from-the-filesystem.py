class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]

        for path in folder[1:]:
            # Check if the current path is subfolder of the last added
            if not path.startswith(res[-1] + '/'):
                res.append(path)

        return res
        