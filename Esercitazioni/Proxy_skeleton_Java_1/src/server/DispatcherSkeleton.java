package server;

import service.IDispatcher;

import java.io.IOException;
import java.net.*;

public abstract class DispatcherSkeleton implements IDispatcher{
    private int port;

    public DispatcherSkeleton(int port){
        this.port = port;
    }

    public void runSkeleton(){
        try{
            ServerSocket serverSocket = new ServerSocket(port);
            
            while(true){
                ServerThread w = new ServerThread(serverSocket.accept(), this);
                w.start();
            }
        }catch(IOException e){
            e.printStackTrace();
        }


    }
}
