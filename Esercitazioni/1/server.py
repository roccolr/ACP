from SkeletonImpl import SkeletonImpl
from SkeletonMagazzino import MagazzinoSkeleton
import threading

if __name__ == '__main__':
    coda_smarphone = []
    coda_laptop = []
    lock = threading.Lock()
    cv_cons_l = threading.Condition(lock)
    cv_cons_s = threading.Condition(lock)
    cv_prod_l = threading.Condition(lock)
    cv_prod_s = threading.Condition(lock)
    skeleton_impl = SkeletonImpl(5, coda_smarphone, coda_laptop, cv_cons_l, cv_prod_l, cv_cons_s, cv_cons_l)
    skeleton = MagazzinoSkeleton(skeleton_impl)

    skeleton.run_skeleton()