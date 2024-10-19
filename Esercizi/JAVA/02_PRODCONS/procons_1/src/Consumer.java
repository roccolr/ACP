public class Consumer extends Thread{
    private Buffer b;
    
    public Consumer(String name, Buffer b){
        super(name);
        this.b=b;
    }

    public void run(){
        b.consuma();
    }
}
