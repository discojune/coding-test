class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        q_logs: Deque = collections.deque()
        q_logs.extend(logs)

        letter_logs = []
        digit_logs = []
        while len(q_logs) >= 1:
            log = q_logs.popleft()
   
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)

        letter_logs = sorted(letter_logs, key=lambda x: (x.split()[1:], x.split()[0]))

        return letter_logs + digit_logs
