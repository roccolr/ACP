package client;

public class Client {
    public static void main(String argv[]){
        Proxycounter proxy = new Proxycounter("127.0.0.1", 6969);
        

        if(argv[0].equals("get")){
            System.out.println("[CLIENT]\trisultato ottenuto: "+proxy.get());
        }
        else if(argv[0].equals("sqr")){
            proxy.square();
            System.out.println("[CLIENT]\tSquare inviato");
        }
        else if(argv[0].equals("sum")){
            proxy.sum(Integer.parseInt(argv[1]));
            System.out.println("[CLIENT]\tInvio richista sum di valore: "+argv[1]);
        }
        else{
            proxy.increment();
            System.out.println("[CLIENT]\tInviato richiesta incremento");
        }
    }
}
