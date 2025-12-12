class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda e: int(e[1]))
        
        mentions = [0] * numberOfUsers
        # offline_until[u] = time when user u becomes online again (exclusive).
        # User is offline at time t if t < offline_until[u].
        offline_until = [0] * numberOfUsers
        
        i = 0
        n = len(events)
        while i < n:
            t = int(events[i][1])
            # gather all events at this timestamp
            j = i
            same_ts = []
            while j < n and int(events[j][1]) == t:
                same_ts.append(events[j])
                j += 1
            
            # 1) Process OFFLINE events first (they take effect immediately at time t)
            for ev in same_ts:
                if ev[0] == "OFFLINE":
                    uid = int(ev[2])
                    if 0 <= uid < numberOfUsers:
                        # reset offline timer to t + 60 (even if already offline)
                        offline_until[uid] = t + 60
            
            # 2) Process MESSAGE events
            for ev in same_ts:
                if ev[0] == "MESSAGE":
                    tokens = ev[2].split()
                    for tok in tokens:
                        if tok == "ALL":
                            # every token occurrence counts — increment everyone
                            for u in range(numberOfUsers):
                                mentions[u] += 1
                        elif tok == "HERE":
                            # mention only users who are online at time t
                            for u in range(numberOfUsers):
                                if not (t < offline_until[u]):  # online if t >= offline_until[u]
                                    mentions[u] += 1
                        elif tok.startswith("id"):
                            # explicit id mentions (may repeat and should be counted each time)
                            try:
                                uid = int(tok[2:])
                            except:
                                continue
                            if 0 <= uid < numberOfUsers:
                                mentions[uid] += 1
                        # ignore any unexpected tokens
            # advance to next timestamp
            i = j
        
        return mentions
