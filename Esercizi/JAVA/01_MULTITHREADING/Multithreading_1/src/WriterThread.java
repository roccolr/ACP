import java.io.*;

public class WriterThread extends Thread{
    private DataOutputStream dataOut;
    public WriterThread(PipedOutputStream dataOut){
        
        this.dataOut = new DataOutputStream(dataOut);
        //nel main creiamo DataOutputStream dataOut, e lo passiamo anche al costruttore di ReaderThread
    }
    public void run(){
        BufferedReader keyboardBuf = new BufferedReader(new InputStreamReader(System.in));
        String s;
        try{
            System.out.println("[WRITER THREAD]\tscrivendo sulla pipe:");
            s = keyboardBuf.readLine();
            dataOut.writeUTF(s);
            System.out.println("[WRITER THREAD]\tscritto: "+s);
        }catch (IOException e){
            e.printStackTrace();
        }
    }
}
