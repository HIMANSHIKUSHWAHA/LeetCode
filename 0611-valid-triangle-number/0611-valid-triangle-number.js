/**
 * @param {number[]} nums
 * @return {number}
 */

function triangleNumber(nums) {
    nums.sort((a, b) => a - b);
    let count = 0;
    const n = nums.length;
    for (let i = n-1; i > 1; i--) {
        let left = 0, right = i-1;
        while (left < right) {
            if (nums[left] + nums[right] > nums[i]) {
                count += right - left;
                right--;
            } else left++;
        }
    }
    return count;
}