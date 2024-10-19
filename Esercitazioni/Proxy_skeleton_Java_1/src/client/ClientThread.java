package client;

import java.util.Random;

public class ClientThread extends Thread{
    private int sleepTime;
    private DispatcherProxy proxy;

    public ClientThread(int sleepTime, DispatcherProxy proxy){
        this.proxy = proxy;
        this.sleepTime = sleepTime;
    }   

    public void run(){
        Random rand = new Random();

        try{
            Thread.sleep(sleepTime*1000);
            // int values [] = {0,1,2,3};
            
            for (int i=0; i<3; i++){
                int cmd = rand.nextInt(4);
                proxy.sendCommand(cmd);
                System.out.println(Thread.currentThread().getName()+" inviato comando: "+cmd);
            }
        }catch(InterruptedException e){
            e.printStackTrace();
        }
    }
}
