//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode sum;
        ListNode* temp = &sum;

        int carry = 0;
        
        while(l1 || l2 || carry){
            //retrieve values of l1 and l2
            int v1 = (l1 ? l1->val : 0);
            int v2 = (l2 ? l2->val : 0);

            //compute the sum of the digits
            int v = v1 + v2 + carry;
            carry = (v / 10);
            v = v % 10;
            temp->next = new ListNode(v);

            //traverse next node
            if(l1) {
                l1 = l1->next;
            };
            if(l2) {
                l2 = l2->next;
            };
            temp = temp->next;
        }

        return sum.next;
    }
};