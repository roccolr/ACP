package server;

import service.Counter;

import java.io.IOException;
import java.net.*;

public abstract class CounterSkeleton implements Counter{
    private int port;

    public CounterSkeleton(int port){
        this.port = port;
    }

    public void run_skeleton(){
        int i = 0;
        try{
            ServerSocket serverSocket = new ServerSocket(port);

            System.out.println("[SKELETON]\tin ascolto sul porto: "+port);
            
            while(true){
                Worker w = new Worker("Thread_"+i, serverSocket.accept(), this);
                w.start();
                i++;
            }
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }
        
    
    }
}
