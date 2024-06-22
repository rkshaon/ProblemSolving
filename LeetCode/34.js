/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// O(log n) solution
let searchRange = function(nums, target) {
    left = binSearch(nums = nums, target = target, isLeftBias = true);
    right = binSearch(nums = nums, target = target, isLeftBias = false);
    
    return [left, right];
};

let binSearch = function (nums, target, isLeftBias) {
    let left = 0;
    let right = nums.length - 1;
    let index = -1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (target > nums[mid]) {
            left = mid + 1;
        } else if (target < nums[mid]) {
            right = mid - 1;
        } else {
            index = mid;

            if (isLeftBias) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
    }
    
    return index;
};

console.log(searchRange(nums = [5, 7, 7, 8, 8, 10], target = 8));
console.log(searchRange(nums = [5, 7, 7, 8, 8, 10], target = 7));
console.log(searchRange(nums = [5, 7, 7, 8, 8, 10], target = 6));
console.log(searchRange(nums = [], target = 0));