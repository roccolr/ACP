package client;

public class Client {
    public static void main(String argv[]){
        String msg = argv[0];
        ProxyCounter proxyCounter = new ProxyCounter();

        if(msg.equals("get")){
            System.out.println("[CLIENT]\tGET:"+proxyCounter.get());
        }
        else if(msg.equals("sum")){
            int value = Integer.parseInt(argv[1]);
            proxyCounter.sum(value);
        }
        else if(msg.equals("sqr")){
            proxyCounter.square();
        }
        else{
            proxyCounter.increment();
        }
    }
}
