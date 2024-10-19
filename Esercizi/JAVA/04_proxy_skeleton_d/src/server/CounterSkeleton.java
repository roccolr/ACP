package server;

import service.Counter;

import java.io.IOException;
import java.net.*;

public class CounterSkeleton implements Counter{
    private CounterImpl counterImpl;

    public CounterSkeleton(CounterImpl counterImpl){
        this.counterImpl = counterImpl;
    }

    public void run_skeleton(){
        try{
            ServerSocket serverSocket = new ServerSocket(6969);
            int i = 0;
            System.out.println("[SERVER]\tRunning on 127.0.0.1:6969");
            while(true){
                ServerWorker w = new ServerWorker("Thread_"+i, serverSocket.accept(), this);
                w.start();
                i++;
            }
        }catch (UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
    public void sum(int val){
        counterImpl.sum(val);
    }
    public int get(){
        return counterImpl.get();
    }
    public void increment(){
        counterImpl.increment();
    }
    public void square(){
        counterImpl.square();
    }
}
