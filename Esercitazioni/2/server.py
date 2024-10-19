from MagazzinoImpl import MagazzinoImpl
import multiprocessing

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    cv_produttore = multiprocessing.Condition(lock)
    cv_consumatore = multiprocessing.Condition(lock)
    q = multiprocessing.Queue(5)
    server = MagazzinoImpl(q, cv_consumatore, cv_produttore)
    server.run_skeleton()