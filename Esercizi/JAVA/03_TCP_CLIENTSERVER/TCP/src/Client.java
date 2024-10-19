import java.io.*;
import java.net.*;;

public class Client extends Thread{
    public static void main(String argv[]){
        //creazione socket
        try{
            System.out.println("[CLIENT]\tCreazione socket");
            Socket s = new Socket("127.0.0.1", 8050);
            System.out.println("[CLIENT]\tSocket Creata");

            System.out.println("[CLIENT]\tCreazione stream di input e output");

            DataInputStream fromServer = new DataInputStream(s.getInputStream());
            DataOutputStream toServer = new DataOutputStream(s.getOutputStream());
            
            System.out.println("[CLIENT]\tMando richiesta al server: ");
            
            toServer.writeUTF("CIAO!");

            System.out.println("[CLIENT]\tAspetto risposta dal server");

            String msg = fromServer.readUTF();
            
            System.out.println("[CLIENT]\tRisposta: "+msg);

            fromServer.close();
            toServer.close();
            s.close();

        }catch (IOException e){
            e.printStackTrace();
        }

    }
}