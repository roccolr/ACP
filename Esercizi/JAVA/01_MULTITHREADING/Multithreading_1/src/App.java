import java.io.*;

public class App {
    // La classe PipedInputStream e PipedOutputStream serve a creare una pipe con la quale 
    // i Threads possono comunicare


    public static void main(String[] args) throws Exception {
        // System.out.println("Hello, World!");
        PipedOutputStream dataOut = new PipedOutputStream();
        WriterThread writerThread = new WriterThread(dataOut);
        ReaderThread readerThread = new ReaderThread(dataOut);

        writerThread.start();
        readerThread.start();
    }
}
