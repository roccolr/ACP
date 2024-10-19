import java.net.*;
import java.io.*;


public class Server{
    public static void main(String argv[]){
        System.out.println("[SERVER]\tCreo la socket");
        try{
            ServerSocket s = new ServerSocket(8050);
            Integer i = 0;
            while(true){
                Socket remote = s.accept();
                Workah w = new Workah(remote, "Worker "+i.toString());
                w.start();
                i+=1;
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
