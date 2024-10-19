package client;

import service.Counter;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;

public class ProxyCounter implements Counter {
    private final String hostRemote = "127.0.0.1";
    private final int port = 6969;

    public void sum(int val){
        try{
            Socket socket = new Socket(hostRemote, port);

            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));

            String msg = "sum";
            toServer.writeUTF(msg);
            toServer.writeInt(val);
            toServer.flush();

            System.out.println("[CLIENT]\tInviato: sum di: "+val);

            toServer.close();
            socket.close();

        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }

    }

    public int get(){
        int x =-1;
        try{
            Socket socket = new Socket(hostRemote, port);
            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));
            DataInputStream fromServer = new DataInputStream(new BufferedInputStream(socket.getInputStream()));

            toServer.writeUTF("get");
            toServer.flush();
            x = fromServer.readInt();

            toServer.close();
            fromServer.close();
            socket.close();
            System.out.println("[CLIENT]\tricevuto valore: "+x);
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }

        return x;
    }

    public void increment(){
        try{
            Socket socket = new Socket(hostRemote, port);
            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));

            toServer.writeUTF("inc");
            toServer.flush();

            toServer.close();
            socket.close();
            System.out.println("[CLIENT]\tInviato: inc");
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }
    }

    public void square(){
        try{
            Socket socket = new Socket(hostRemote, port);
            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));

            toServer.writeUTF("sqr");
            toServer.flush();

            toServer.close();
            socket.close();
            System.out.println("[CLIENT]\tInviato: sqr");

        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }

    }
}