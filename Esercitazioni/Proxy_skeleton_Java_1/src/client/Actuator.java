package client;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;


public class Actuator {
    public static void main(String[] args) {
        DispatcherProxy proxy = new DispatcherProxy();
        int cmd = -1;
        try{
            FileOutputStream toFile = new FileOutputStream("/home/studente/Desktop/acp/Esercitazioni/Proxy_skeleton_Java_1/storage/cmdLog.txt", true);
            PrintStream outStream = new PrintStream(toFile);

            
            while(true){
                
                cmd = proxy.getCommand();
                System.out.println("[DISPATCHER]\tottenuto comando "+cmd);
                try{
                    outStream.println("command: "+cmd);
                    outStream.flush();
                    Thread.sleep(1000);
                    
                }catch(InterruptedException e){
                    e.printStackTrace();
                }
            }
            
        }catch(FileNotFoundException e){
            e.printStackTrace();
        }
        
        
    }
}
