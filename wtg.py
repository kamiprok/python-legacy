import py4chan


board = py4chan.Board('vg')
print(board)

print(board.Name)
print(board.getThreads(page=1))

# for thread in board.getThreads(page=0):
#     print(thread.id, thread.topic)
#
# thread = board.getThreads(page=1)
# print(thread)
