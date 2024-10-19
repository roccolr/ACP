package server;

import service.Counter;

public class CounterImpl implements Counter{
    private int value;

    public CounterImpl(){
        value = 0;
    }

    public void sum(int val){
        value += val;
    }
    public int get(){
        return value;
    }
    public void increment(){
        value++;
    }
    public void square(){
        value *= value;
    }
}
