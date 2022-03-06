#include <vector>
#include <set>

using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    int pocketmon_num = nums.size();
    int max_get = pocketmon_num / 2;
    set<int> my_pocketmon;
    
    for (size_t i = 0; i < pocketmon_num; i++)
    {
        my_pocketmon.insert(nums[i]);
    }
    
    int n = my_pocketmon.size();

    if (n >= max_get) {
        answer = max_get;
    } else {
        answer = n;
    }

    return answer;
}