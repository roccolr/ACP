package server;

public class CounterImpl extends CounterSkeleton{
    private int value;

    public CounterImpl(int port){
        super(port);
        value = 0;
    }

    public int get(){
        return value;
    }

    public void increment(){
        value = value +1;
    }

    public void square(){
        value = value*value;
    }

    public void sum(int x){
        value = value+x;
    }
}
