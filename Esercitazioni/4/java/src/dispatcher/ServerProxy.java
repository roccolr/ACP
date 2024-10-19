package dispatcher;

import interfaccia.IServer;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;

public class ServerProxy implements IServer{
    public void deposita(int value){
        try{
            Socket s = new Socket("127.0.0.1", 6969);
            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
            String msg = "deposita-"+value;
            toServer.writeUTF(msg);
            toServer.flush();
            System.out.println("[DISPATCHER]\tinviato il messaggio "+msg);
            s.close();
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }

    }   
    public int preleva(){
        int res = -1;
        try{
            Socket s = new Socket("127.0.0.1", 6969);
            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
            BufferedReader fromServer = new BufferedReader(new InputStreamReader(s.getInputStream()));
            String msg = "preleva";
            toServer.writeUTF(msg);
            toServer.flush();
            String valueString = fromServer.readLine();
            System.out.println("[DISPATCHER]\tRicevuto il valore "+valueString);
            res = Integer.parseInt(valueString);
            s.close();
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException e){
            e.printStackTrace();
        }
        return res;
    }
}
