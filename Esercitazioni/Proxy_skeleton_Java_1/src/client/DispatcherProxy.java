package client;

import service.IDispatcher;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;

public class DispatcherProxy implements IDispatcher{


    public void sendCommand(int cmd){
        try{
            Socket s = new Socket("127.0.0.1", 6969);
            
            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));

            toServer.writeUTF("cmd");
            toServer.writeInt(cmd);
            toServer.flush();

            toServer.close();
            s.close();

        }catch (IOException e){
            e.printStackTrace();
        }
            
        
    }
    public int getCommand(){
        int cmd = -1;
        try{
            Socket s = new Socket("127.0.0.1", 6969);

            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
            DataInputStream fromServer = new DataInputStream(new BufferedInputStream(s.getInputStream()));

            toServer.writeUTF("get");
            toServer.flush();
            System.out.println("mandato Get");
            cmd = fromServer.readInt();
            System.out.println("proxy\tRicevuto comando dal server: "+cmd);
            toServer.close();
            fromServer.close();
            s.close();
        }catch(IOException e){
            e.printStackTrace();
        }
        return cmd;
    }
}
