package server;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;

public class ServerWorker extends Thread{
    private CounterSkeleton skeleton;
    private Socket socket;

    public ServerWorker(String name, Socket socket,CounterSkeleton skeleton){
        super(name);
        this.skeleton = skeleton;
        this.socket = socket;
    }

    public void run(){
        try{
            DataOutputStream toClient = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));
            DataInputStream fromClient = new DataInputStream(new BufferedInputStream(socket.getInputStream()));

            String msg = fromClient.readUTF();
            if(msg.equals("get")){
                int x = skeleton.get();
                toClient.writeInt(x);
                toClient.flush();
            }
            else if(msg.equals("inc")){
                skeleton.increment();
            }
            else if(msg.equals("sum")){
                int value = fromClient.readInt();
                skeleton.sum(value);
            }else{
                skeleton.square();
            }
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
