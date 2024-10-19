package client;

import service.Counter;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;

public class Proxycounter implements Counter{
    private String hostname;
    private int port;

    public Proxycounter(String hostname, int port){
        this.hostname = hostname;
        this.port=port;
    }


    public void increment(){

        try{
            Socket socket = new Socket(hostname, port);
            
            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));
            // DataInputStream fromServer = new DataInputStream(new BufferedInputStream(socket.getInputStream()));
            toServer.writeUTF("inc");
            toServer.flush();
            toServer.close();
            socket.close();
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }
    }

    public int get(){
        int x = -1;

        try{
            Socket socket = new Socket(hostname, port); //crea la socket e la connette a hostname e port

            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));
            DataInputStream fromServer = new DataInputStream(new BufferedInputStream(socket.getInputStream()));

            toServer.writeUTF("get");
            toServer.flush();
            x = fromServer.readInt();

            toServer.close();
            fromServer.close();
            socket.close();
        }catch (UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }
        return x;
    }

    public void sum(int val){
        try{
            Socket socket = new Socket(hostname, port);

            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));

            toServer.writeUTF("sum");
            toServer.writeInt(val);
            toServer.flush();
            
            toServer.close();
            socket.close();
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }
    }

    public void square(){
        try{
            Socket socket = new Socket(hostname, port);
            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(socket.getOutputStream()));
            toServer.writeUTF("sqr");
            toServer.flush();

            toServer.close();
            socket.close();
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
    
}
