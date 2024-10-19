import java.io.*;

public class ReaderThread extends Thread {
    private DataInputStream dataIn;

    public ReaderThread(PipedOutputStream pipeOut){
        try{
            dataIn = new DataInputStream(new PipedInputStream(pipeOut));

        }catch (IOException e){
            // System.out.println(e);
            e.printStackTrace();
        }
    }

    public void run(){
        String s;
        try{
            System.out.println("[READER THREAD]\taspettando un messaggio sulla pipe");
            s = dataIn.readUTF();
            System.out.println("[READER THREAD]\tRicevuto:"+s);
        }catch (IOException e){
            // System.out.println();
            e.printStackTrace();
        }
    }

}
