class Solution {
public:
    ListNode* reverse(ListNode* head){
        if(head == NULL || head->next == NULL) return head;
        ListNode* newHead = reverse(head->next);
        ListNode* front = head->next;
        front->next = head;
        head->next = NULL;

        return newHead;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode *dummy = new ListNode(99);
        dummy->next = head;
        ListNode *prev = dummy;
        while(head){
            ListNode* ptr = head;
            int count = 0;
            while(count < k - 1 && ptr){
                count++;
                ptr = ptr->next;
                
            }
            if(!ptr) break;
            
            ListNode* temp = ptr->next;
            ptr->next = NULL;
            ListNode* rev = reverse(head);
            prev->next = rev;
            prev = head;
            head->next = temp;
            head = temp;
            
        }
        return dummy->next;

    }
};