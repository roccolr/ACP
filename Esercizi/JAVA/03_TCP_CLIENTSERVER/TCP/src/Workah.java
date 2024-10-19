import java.net.*;
import java.io.*;

public class Workah extends Thread{
    private Socket sock;

    public Workah(Socket s, String name){
        super(name);
        sock = s;
    }

    public void run(){
        //creazione flussi in entrata e in uscita
        try{
            DataInputStream fromClient = new DataInputStream(sock.getInputStream());
            DataOutputStream toClient = new DataOutputStream(sock.getOutputStream());  
            SocketAddress remoteSocket = sock.getRemoteSocketAddress();

            String msg = fromClient.readUTF();            
            System.out.println(Thread.currentThread().getName()+"\tRicevuto da "+remoteSocket.toString()+" messaggio: "+msg);
            toClient.writeUTF("CIAO A TE DA "+Thread.currentThread().getName());
            System.out.println(Thread.currentThread().getName()+"\tRisposta inviata");

            toClient.close();
            fromClient.close();
            sock.close();

        }catch (IOException e){
            e.printStackTrace();
        }



    }


}
