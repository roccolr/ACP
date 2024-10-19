package server;

public class Server {
    public static void main(String argv[]){
        CounterImpl counterImpl = new CounterImpl();
        CounterSkeleton counterSkeleton = new CounterSkeleton(counterImpl);
        counterSkeleton.run_skeleton();
    }
}
