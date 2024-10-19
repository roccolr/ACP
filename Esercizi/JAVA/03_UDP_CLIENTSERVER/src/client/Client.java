package client;
import java.io.IOException;
import java.net.*;


public class Client {
    public static void main(String argv[]){ 
        
        try{
            //creazione socket per inviare
            DatagramSocket socket = new DatagramSocket();
            

            //creazione del datagramma da inviare
            byte [] payload  = "Hello world".getBytes();

            //creazione del datagramma
            DatagramPacket pkg = new DatagramPacket(payload, payload.length, InetAddress.getLocalHost(), 6969);

            //inviamo il pacchetto
            socket.send(pkg);

            //riceviamo il pacchetto
            byte [] received = new byte[65508];
            DatagramPacket receivedPkg = new DatagramPacket(received, 65508);
            socket.receive(receivedPkg);

            int fromPort = receivedPkg.getPort();
            InetAddress fromAddress = receivedPkg.getAddress();
            String msg = new String(received);

            System.out.println("[CLIENT]\tricevuto: "+msg+" da:"+fromAddress.toString()+":"+fromPort);

            socket.close();

        }catch (SocketException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }
    }
}
