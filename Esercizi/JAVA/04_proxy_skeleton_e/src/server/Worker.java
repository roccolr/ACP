package server;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;

public class Worker extends Thread{
    Socket socket;
    CounterSkeleton skeleton;
    public Worker(String name, Socket socket, CounterSkeleton skeleton){
        super(name);
        this.socket = socket;
        this.skeleton = skeleton;
    }

    public void run(){
        int x = -1;
        try{
            DataInputStream fromClient = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
            DataOutputStream toClient = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));
            String msg = fromClient.readUTF(); 
            if (msg.equals("get")){
                x = skeleton.get();
                toClient.writeInt(x);
                toClient.flush();
            }
            else if (msg.equals("inc")){
                skeleton.increment();
            }
            else if (msg.equals("sum")){
                x = fromClient.readInt();
                skeleton.sum(x);
            }
            else{
                skeleton.square();
            }

            fromClient.close();
            socket.close();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
