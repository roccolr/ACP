package client;

import java.util.Random;

public class Client {
    public static void main(String[] args) {
        Random rand = new Random();
        DispatcherProxy proxy = new DispatcherProxy();
        ClientThread [] threads = new ClientThread[5];
        
        for (int i=0; i<5; i++){
            int sleepTime = rand.nextInt(3)+2;
            threads[i] = new ClientThread(sleepTime, proxy);
            threads[i].start();
        }

        for(ClientThread thread: threads){
            try{
                thread.join();
                System.out.println("[MAIN CLIENT]\tjoinato thread");
            }catch(InterruptedException e){
                e.printStackTrace();
            }
            
        }
    }
}
