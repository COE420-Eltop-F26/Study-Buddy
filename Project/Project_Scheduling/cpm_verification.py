"""Recomputes the StudyBuddy schedule (forward pass, backward pass, slack, critical paths)
from the same task list, durations and predecessors as WBS.md."""
tasks = {  # id: (duration in days, predecessors)
    "T1": (2, []), "T2": (3, ["T1"]), "T3": (3, ["T1"]), "T4": (4, ["T2", "T3"]),
    "T5": (5, ["T4"]), "T6": (3, ["T4"]), "T7": (5, ["T5", "T6"]), "T8": (4, ["T5"]),
    "T9": (4, ["T8"]), "T10": (2, ["T6"]), "T11": (4, ["T7", "T9", "T10"]),
}
ids = list(tasks)
succ = {i: [j for j in ids if i in tasks[j][1]] for i in ids}
ES, EF, LS, LF = {}, {}, {}, {}
for i in ids:                                   # forward pass
    ES[i] = max((EF[p] for p in tasks[i][1]), default=0)
    EF[i] = ES[i] + tasks[i][0]
end = max(EF.values())
for i in reversed(ids):                         # backward pass
    LF[i] = min((LS[s] for s in succ[i]), default=end)
    LS[i] = LF[i] - tasks[i][0]
print("Task  E  ES  EF  LS  LF  Slack")
for i in ids:
    print(f"{i:<5}{tasks[i][0]:>2}{ES[i]:>4}{EF[i]:>4}{LS[i]:>4}{LF[i]:>4}{LS[i]-ES[i]:>6}")
print("Project duration:", end, "days")

def paths(i, p=()):
    p += (i,)
    if not succ[i]:
        yield p
    for s in succ[i]:
        yield from paths(s, p)

for start in [i for i in ids if not tasks[i][1]]:
    for p in paths(start):
        d = sum(tasks[i][0] for i in p)
        print(" -> ".join(p), d, "CRITICAL" if d == end else "")
