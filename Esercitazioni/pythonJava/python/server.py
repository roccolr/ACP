import RealDispatcher
import multiprocessing

if __name__ == '__main__':
    q = multiprocessing.Queue(5)
    skeleton = RealDispatcher.RealDispatcher(q)
    skeleton.run_skeleton()