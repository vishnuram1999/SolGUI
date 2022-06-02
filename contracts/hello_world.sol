// SPDX-License-Identifier: CC-BY-SA-4.0
pragma solidity >=0.8.13;
contract hello_world {
    string hello_string = "HELLO_WORLD!";
    function hello() view public returns (string memory) {
        return hello_string;
    }
}