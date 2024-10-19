from ServerImpl import ServerImpl
import multiprocessing

if __name__ == '__main__':
    queue = multiprocessing.Queue(5)
    skeleton = ServerImpl(queue=queue)
    skeleton.run_skeleton()