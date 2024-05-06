#[starknet::interface]
trait ICounter<T> {
    // Returns the current counter value.
    fn get_counter(self: @T) -> u32;
    // Increases the counter by 1.
    fn increase_counter(ref self: T);
    // Decreases the counter by 1.
    fn decrease_counter(ref self: T);
}

#[starknet::contract]
mod Counter {
    use traits::Into;

    #[storage]
    struct Storage {
        counter: u32,
    }

    #[constructor]
    fn constructor(ref self: ContractState, initial_value: u32) {
        self.counter.write(initial_value);
    }

    #[abi(embed_v0)]
    impl Counter of super::ICounter<ContractState> {
        fn get_counter(self: @ContractState) -> u32 {
            self.counter.read()
        }

        fn increase_counter(ref self: ContractState) {
            self.counter.write(self.counter.read() + 1);
        }

        fn decrease_counter(ref self: ContractState) {
            self.counter.write(self.counter.read() - 1);
        }
    }
}