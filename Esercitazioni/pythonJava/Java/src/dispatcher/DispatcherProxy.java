package dispatcher;

import java.io.BufferedOutputStream;
import java.io.BufferedReader;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;

public class DispatcherProxy {
    public void deposita(int val){
        try{
            Socket s = new Socket("127.0.0.1", 6969);

            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
            toServer.writeUTF("deposita-"+val);
            toServer.flush();

            System.out.println("[DISPATCHER PROXY]\tinviata richiesta di deposito");

            toServer.close();
            s.close();
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch (IOException i){
            i.printStackTrace();
        }
    }
    public int preleva(){
        int value = -1;
        try{
            Socket s = new Socket("127.0.0.1", 6969);

            DataOutputStream toServer = new DataOutputStream(new BufferedOutputStream(s.getOutputStream()));
            BufferedReader fromServer = new BufferedReader(new InputStreamReader(s.getInputStream()));

            toServer.writeUTF("preleva");
            toServer.flush();
            String msgBack = new String(fromServer.readLine());
            value = Integer.parseInt(msgBack); 

            s.close();
        }catch(UnknownHostException e){
            e.printStackTrace();
        }catch(IOException i){
            i.printStackTrace();
        }
        return value;
    }
}
