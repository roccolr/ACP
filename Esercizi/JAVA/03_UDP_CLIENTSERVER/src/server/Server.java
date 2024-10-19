package server;

import java.io.IOException;
import java.net.*;
import java.util.ArrayList;

public class Server {
    public static void main(String argv[]){
        try{
            DatagramSocket socket = new DatagramSocket(6969);
            byte [] buffer = new byte[65508];
            int i = 0;
            ArrayList<Worker> workers = new ArrayList<>();
            while(true && i<10){
                DatagramPacket rcv = new DatagramPacket(buffer, buffer.length);
                socket.receive(rcv);
                workers.add(new Worker("THREAD_"+i, rcv.getData(), rcv.getAddress(), rcv.getPort()));
                workers.get(i).start();
                i++;
            }

            for (Worker w : workers){
                w.join();
            }
            socket.close();

            System.out.println("FINE SERVER");
        }catch (IOException e){
            e.printStackTrace();
        }catch (InterruptedException e){
            e.printStackTrace();
        }
    }
}
