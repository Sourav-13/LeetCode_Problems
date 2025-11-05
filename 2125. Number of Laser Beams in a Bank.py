class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        size =  len(bank) 
        ans = 0
        start = 0
        end = 1
        while True:
            if(end >= size):
                break
            
            upper_row = bank[start].count("1")
            if not upper_row:
                start += 1
                end += 1
                continue
            
            lower_row = bank[end].count("1")
            if not lower_row:
                end += 1
                continue
            
            ans += lower_row * upper_row
            start = end
            end += 1
        return ans
    
    

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        
        total_beams = 0
        prev_device_count = 0
        
        for row in bank:
            # 1. Count devices in the current row
            current_device_count = row.count('1')
            
            # 2. If this row is empty, skip it.
            #    We keep our 'prev_device_count' and hope
            #    the next row has devices.
            if current_device_count == 0:
                continue
            
            # 3. If this row has devices, add the beams
            #    connecting it to the previous non-empty row.
            total_beams += (prev_device_count * current_device_count)
            
            # 4. Update the 'previous' count to be this row's
            #    count for the next iteration.
            prev_device_count = current_device_count
            
        return total_beams