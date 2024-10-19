package server;

public class Server {
    public static void main(String argv[]){
        CounterImpl coutnerImpl = new CounterImpl(6969);
        System.out.println("[SERVER]\trunning on localhost:6969");
        coutnerImpl.run_skeleton();
    }
    
}
