package server;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;

public class ServerThread extends Thread{
    Socket s;
    DispatcherSkeleton skeleton;

    public ServerThread(Socket s, DispatcherSkeleton skeleton){
        this.s = s;
        this.skeleton = skeleton;
    }

    public void run(){
        try{
            DataOutputStream toClient = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
            DataInputStream fromClient = new DataInputStream(new BufferedInputStream(s.getInputStream()));
            String messageFromClient = fromClient.readUTF();

            if(messageFromClient.equals("cmd")){
                int cmd = fromClient.readInt();
                skeleton.sendCommand(cmd);
            }else if (messageFromClient.equals("get")){
                int cmdToClient = skeleton.getCommand();
                toClient.writeInt(cmdToClient);
                toClient.flush();
                System.out.println("inviato con successo all'attuatore il valore: "+cmdToClient);
            }else{
                System.out.println(Thread.currentThread().getName()+" Comando non riconosciuto");
            }
            
        }catch(IOException e){
            e.printStackTrace();
        }

    }
}
