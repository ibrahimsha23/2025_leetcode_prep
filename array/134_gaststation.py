class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # finding starting point
        strt_index = None
        origin_point = None
        len_gas_station = len(gas)
        for i in range(len_gas_station):
            if gas[i] >= cost[i]:
                strt_index = i
                origin_point = i
                break;

        gas_capacity = 0
        cost_capacity = 0
        is_travel = True
        while is_travel:
            gas_capacity += gas[strt_index] - cost_capacity
            cost_capacity = cost[strt_index]
            next_idx = (strt_index+1) %  len_gas_station
            print("index", strt_index, next_idx)
            print("gas_capacity", gas_capacity)
            strt_index = next_idx
            is_travel = False if origin_point == next_idx else True
        if gas_capacity >= cost_capacity:
            return origin_point

if __name__ == "__main__":
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    sol = Solution()
    result = sol.canCompleteCircuit(gas, cost)
    print(result)