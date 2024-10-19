package server;
import java.io.IOException;
import java.net.*;

public class Worker extends Thread{
    private byte[] data;
    private InetAddress address;
    private int port;

    public Worker(String name, byte[] data, InetAddress address, int port){
        super(name);
        this.data = data;
        this.address = address;
        this.port = port;
    }

    public void run(){
        System.out.println(Thread.currentThread().getName()+"\tricevuto msg: "+new String(data)+" da: "+address.toString()+":"+port);
        
        data = ("CIAO DA "+Thread.currentThread().getName()).getBytes();
        try{
            DatagramPacket resPkg = new DatagramPacket(data, data.length, InetAddress.getLocalHost(), port);
            DatagramSocket socket = new DatagramSocket();
            socket.send(resPkg);
            System.out.println(Thread.currentThread().getName()+"\tinviato msg: "+new String(data)+" a: "+resPkg.getAddress().toString()+":"+resPkg.getPort());
            socket.close();
        }catch (SocketException e){
            e.printStackTrace();
        }catch (UnknownHostException e){
            e.printStackTrace();
        }catch (IOException e){
            e.printStackTrace();
        }
     }
}
