static class Singleton {
    private final static Singleton singleton = new Singleton();
    private String value;

    private Singleton() {}

    public static Singleton getInstance() {
        return singleton;
    }

    public String getValue() {
        return this.value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    
}
