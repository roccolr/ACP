public class App {
    public static void main(String[] args) throws Exception {

        //creiamo il buffer

        Buffer b = new Buffer();

        for(int i=0; i<3; i++){
            Integer i_integer = new Integer(i);
            Producer p = new Producer(b, "Producer "+i_integer.toString());
            p.start();
        }

        for(int i=0; i<3; i++){
            Integer i_integer = new Integer(i);
            Consumer c = new Consumer( "Consumer "+i_integer.toString(),b);
            c.start();
        }
    }
}
