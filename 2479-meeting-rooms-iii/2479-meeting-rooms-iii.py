import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
        
        # Min-heap for available rooms by room index
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)

        # Min-heap for occupied rooms by end time: (end_time, room_index)
        occupied_rooms = []

        # Count of meetings each room has hosted
        room_meeting_count = [0] * n

        for start, end in meetings:
            # Free up rooms whose meetings have ended before current start time
            while occupied_rooms and occupied_rooms[0][0] <= start:
                end_time, room_id = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room_id)

            if available_rooms:
                # If room is available, assign it
                room_id = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, (end, room_id))
                room_meeting_count[room_id] += 1
            else:
                # No room is free, delay meeting to earliest room free time
                earliest_end_time, room_id = heapq.heappop(occupied_rooms)
                duration = end - start
                new_end_time = earliest_end_time + duration
                heapq.heappush(occupied_rooms, (new_end_time, room_id))
                room_meeting_count[room_id] += 1

        # Return room with most meetings (lower index wins tie)
        max_meetings = max(room_meeting_count)
        for i in range(n):
            if room_meeting_count[i] == max_meetings:
                return i
