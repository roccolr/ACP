import multiprocess

def parent(parent_conn):
    parent_conn.send(10)
    parent_conn.close()

def child(child_conn):
    print(child_conn.recv())
    child_conn.close()


if __name__ == '__main__':
    (child_conn, parent_conn) = multiprocess.Pipe()
    p1 = multiprocess.Process(target = parent, args = (parent_conn,))
    p2 = multiprocess.Process(target = child, args = (child_conn,))

    p1.start()
    p2.start()


    p1.join()
    p2.join()

