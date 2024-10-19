package server;
import coda.interfaccia.*;
import coda.implementazioni.*;

public class Server {
    public static void main(String[] args) {
        Coda coda = new CodaCircolare(5);
        CodaWrapper wrapper = new CodaWrapperSynch(coda);

        DispatcherImpl skeleton = new DispatcherImpl(6969, wrapper);
        System.out.println("[SERVER]\trunning on port "+6969);
        skeleton.runSkeleton();
    }
}
